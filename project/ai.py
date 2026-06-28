import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = r"Phi_3.5_instruct/"

device_phi = "cuda:0"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    trust_remote_code=True,
    attn_implementation="flash_attention_2",
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    device_map={"": device_phi}
)


def analyze(company, price, pe, market_cap, dividend):

    prompt = f"""
              SYSTEM:
              You are a financial analyst AI.

              You MUST ONLY produce financial analysis.

              You are STRICTLY FORBIDDEN to write essays, macroeconomics explanations, or general theory.

              OUTPUT FORMAT (STRICT):
              Overview:
              Financial Health:
              Strengths:
              Weaknesses:
              Risks:
              Valuation:
              Technical Analysis:
              Final Decision:
              Score (0-10):
              Recommendation (BUY / HOLD / SELL):

              RULES:
              - No introductions
              - No extra text
              - No macroeconomics
              - Be concise and data-driven

              USER:
              Company: {company}
              Price: {price}
              P/E Ratio: {pe}
              Market Cap: {market_cap}
              Dividend: {dividend}

              ANSWER:
              """

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True
    ).to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=650,
            temperature=0.1,
            top_p=0.9,
            do_sample=True
        )

    generated_tokens = output[0][inputs["input_ids"].shape[-1]:]
    decoded = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()

    # safety cleanup (evita output fuori formato)
    if "Instruction" in decoded:
        decoded = decoded.split("Instruction")[0]

    return decoded
