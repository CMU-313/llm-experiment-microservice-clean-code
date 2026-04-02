complete_eval_set = [

    # 16 Non-English posts covering 8 languages

    # German
    {
        "post": "Hier ist dein erstes Beispiel.",
        "expected_answer": (False, "This is your first example.")
    },
    # French
    {
        "post": "Bonjour, comment vous appelez-vous?",
        "expected_answer": (False, "Hello, what is your name?")
    },
    {
        "post": "Où est la bibliothèque la plus proche?",
        "expected_answer": (False, "Where is the nearest library?")
    },
    {
        "post": "Je voudrais commander un café, s'il vous plaît.",
        "expected_answer": (False, "I would like to order a coffee, please.")
    },
    # Spanish
    {
        "post": "Me llamo Squidward y soy de España.",
        "expected_answer": (False, "My name is Squidward and I am from Spain.")
    },
    {
        "post": "¿Puedes ayudarme con mi tarea?",
        "expected_answer": (False, "Can you help me with my homework?")
    },
    {
        "post": "El mercado abre a las ocho de la mañana.",
        "expected_answer": (False, "The market opens at eight in the morning.")
    },
    # Japanese
    {
        "post": "今日は良い天気ですね。",
        "expected_answer": (False, "The weather is nice today, isn't it?")
    },
    {
        "post": "私はコンピューターサイエンスを勉強しています。",
        "expected_answer": (False, "I am studying computer science.")
    },
    # Russian
    {
        "post": "Я люблю читать книги.",
        "expected_answer": (False, "I love reading books.")
    },
    {
        "post": "Пожалуйста, говорите медленнее.",
        "expected_answer": (False, "Please speak more slowly.")
    },
    # Korean
    {
        "post": "저는 학생입니다.",
        "expected_answer": (False, "I am a student.")
    },
    {
        "post": "오늘 날씨가 정말 좋네요.",
        "expected_answer": (False, "The weather is really nice today.")
    },
    # Portuguese
    {
        "post": "O gato está em cima da mesa.",
        "expected_answer": (False, "The cat is on top of the table.")
    },
    {
        "post": "Preciso de ajuda com o meu projeto.",
        "expected_answer": (False, "I need help with my project.")
    },
    # Italian
    {
        "post": "Ciao, come stai?",
        "expected_answer": (False, "Hello, how are you?")
    },
    {
        "post": "Vorrei prenotare un tavolo per due persone.",
        "expected_answer": (False, "I would like to book a table for two people.")
    },

    # 15 English posts
    {
        "post": "Hello, how are you doing today?",
        "expected_answer": (True, "Hello, how are you doing today?")
    },
    {
        "post": "Can anyone recommend a good textbook for machine learning?",
        "expected_answer": (True, "Can anyone recommend a good textbook for machine learning?")
    },
    {
        "post": "I just finished reading a great novel last night.",
        "expected_answer": (True, "I just finished reading a great novel last night.")
    },
    {
        "post": "The forum has been really helpful for my research.",
        "expected_answer": (True, "The forum has been really helpful for my research.")
    },
    {
        "post": "Does anyone know when the next version will be released?",
        "expected_answer": (True, "Does anyone know when the next version will be released?")
    },
    {
        "post": "I have been struggling with this bug for two days.",
        "expected_answer": (True, "I have been struggling with this bug for two days.")
    },
    {
        "post": "Please check the documentation before posting your question.",
        "expected_answer": (True, "Please check the documentation before posting your question.")
    },
    {
        "post": "What are the best practices for writing clean code?",
        "expected_answer": (True, "What are the best practices for writing clean code?")
    },
    {
        "post": "I agree with the previous comment, the API is well-designed.",
        "expected_answer": (True, "I agree with the previous comment, the API is well-designed.")
    },
    {
        "post": "Could you share the link to the original paper?",
        "expected_answer": (True, "Could you share the link to the original paper?")
    },
    {
        "post": "The installation process was straightforward on Linux.",
        "expected_answer": (True, "The installation process was straightforward on Linux.")
    },
    {
        "post": "This tutorial helped me understand the concept much better.",
        "expected_answer": (True, "This tutorial helped me understand the concept much better.")
    },
    {
        "post": "Looking forward to the upcoming workshop on distributed systems.",
        "expected_answer": (True, "Looking forward to the upcoming workshop on distributed systems.")
    },
    {
        "post": "Has anyone tried running this on an ARM-based machine?",
        "expected_answer": (True, "Has anyone tried running this on an ARM-based machine?")
    },
    {
        "post": "Thanks for the detailed explanation, it really cleared things up.",
        "expected_answer": (True, "Thanks for the detailed explanation, it really cleared things up.")
    },

    # 6 Malformed / unintelligible posts

    # Random symbols (not any recognizable language)
    {
        "post": "@#$%^&*()!~`",
        "expected_answer": (True, "@#$%^&*()!~`")
    },
    # Numbers only
    {
        "post": "1234567890",
        "expected_answer": (True, "1234567890")
    },
    # Emojis only
    {
        "post": "😀🎉🤔💡🚀",
        "expected_answer": (True, "😀🎉🤔💡🚀")
    },
    # Keyboard-mash text
    {
        "post": "asdfjkl; qwerty zxcvbnm",
        "expected_answer": (True, "asdfjkl; qwerty zxcvbnm")
    },
    # Empty post (whitespace only)
    {
        "post": "   ",
        "expected_answer": (True, "   ")
    },
    # Mixed symbols and digits
    {
        "post": "42 ??? !!!... 0x1F",
        "expected_answer": (True, "42 ??? !!!... 0x1F")
    },
]
