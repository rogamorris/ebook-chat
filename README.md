# ebook-chat
This is a web app that allows you to upload an ebook and ask questions about it using a chat interface. I relied heavily on ChatGPT (GPT-4) in building it. My motivation was to practice building web apps using ChatGPT, and I thought it would be cool if I could eventually have a tool that I can upload my favorite non-fiction books to and ask questions about them.

Here's the initial prompt I used, which I thought worked quite well:
Please act as an expert full-stack web developer who is teaching me to build a web app using React and Flask, step by step. A few things to keep in mind: work as iteratively as possible by having me test each step to ensure it works before proceeding to the next step. Instruct me to commit code to GitHub after each step. Thoroughly comment any code you write so I understand what it does.

The goal is to build a web app that allows a user to upload a non-fiction ebook and ask anything about the book with chat interface, using the OpenAI API. 

Here is a description of the basic requirements.

Requirement 1: User can select and upload an ebook from their computer
* Only allow files in EPUB format to be uploaded
* Return an error letting a user know if the EPUB file they uploaded is unreadable (this could be due to DRM protection or missing/corrupt data)
* Return an error letting a user know if they have exceeded the max file size (for now, let’s set the max file size to 15 MB)

Requirement 2: Once an ebook has been uploaded, the app uses OpenAI API and the best available chunking/summarization techniques to understand the content of the ebook
* The finished app should be capable of clearly and accurately summarizing a book that has millions of words.
* The finished app should also understand specific concepts or ideas in the book and either explain or expand on those ideas
* Make sure the summarization logic is in it’s own module so it can be iteratively improved without affecting the rest of the app

Requirement 3: User can ask questions about the book they uploaded using a ChatGPT-like interface

The above are the basic requirements, please ask any clarifying questions before we get started with working on this project.

## To Do
- Right now, you can only upload EPUB files that are shorter than GPT-3.5-Turbo's context window. I still need to figure out how to implement logic that divides a book down into smaller chunks and summarizes each chunk so you can use the app with normal-lenght books.
- I want to make the chat interface look a lot better
- I'm considering other features, such as the ability to upload different content types (youtube or article link), ability to ask questions across multiple content sources (e.g. imagine you wanted to synthesize multiple books).
