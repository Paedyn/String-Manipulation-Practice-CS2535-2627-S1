module = "navigation|life_support|cargo_bay|engine_control"

module= module.replace("_", " ")

module = module.split("|")
text =", ".join(module)
print(text.title())
