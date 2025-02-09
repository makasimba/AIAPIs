import replicate

input = {
    "prompt": "What is the speed of an unladen swallow?"
}

for event in replicate.stream(
    "deepseek-ai/deepseek-r1",
    input=input
):
    print(event, end="")