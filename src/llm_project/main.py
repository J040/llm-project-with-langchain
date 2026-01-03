def main():
    from langchain_ollama import ChatOllama
    from langchain_core.messages import HumanMessage, SystemMessage
    from langcahin_core.prompts import promptTemplate

    llm = ChatOllama(
        model="llama3.2:latest",
        temperature=0.2
    )

    system_msg = SystemMessage('''You're an art teacher.''')
    human_msg = HumanMessage('''How to paint?''')

    response = llm.invoke([system_msg, human_msg])
    print(response.content)

if __name__ == "__main__":
    main()