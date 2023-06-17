import openai
import argparse
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['OPEN_AI_API_KEY']


def get_response(messages):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return res

def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end

def blue(text):
    blue_start = "\033[94m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end

def red(text):
    red_start = "\033[91m"
    red_end = "\033[0m"
    return red_start + text + red_end

def main():
    messages = []

    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument('--personality', type=str, help='Brief description of the personality',
                        default="You are a friendly and helpful chatbot")
    args = parser.parse_args()

    print("Personality: ", args.personality)

    initial_prompt = f"""
        You are a chatbot who is really good at roleplaying. 
        You are soo good that you never tell that your are roleplaying and keep your role going.
        Your personality is {args.personality}
    """
    
    messages.append({"role": "system", "content": initial_prompt})

    while True:
        try:
            user_input = input(blue("You: "))
            messages.append({"role": "user", "content": user_input})
            res = get_response(messages)
            messages.append(res['choices'][0]['message'].to_dict())
            resData = res['choices'][0]['message']
            # print("Message History", messages)
            print(red("Bot: ") + bold(resData['content']))

        except KeyboardInterrupt:
            print("Bye!")
            break


if __name__ == '__main__':
    main()
