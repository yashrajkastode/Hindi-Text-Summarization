📝 Hindi Text Summarizer (हिंदी टेक्स्ट सारांश)
A streamlined React application designed to provide concise summaries of long Hindi text using an AI-driven backend API.

🚀 Features
Hindi Language Support: Specifically optimized for Devanagari script processing.

Asynchronous Processing: Uses a polling mechanism to check the status of summarization tasks.

Real-time Feedback: Includes a loading state and error handling for a smooth user experience.

Responsive UI: Built with a "mobile-first" approach using Tailwind CSS for clean presentation on all devices.

🛠️ Tech Stack
Frontend: React (Vite)

Styling: Tailwind CSS

Build Tools: PostCSS, Autoprefixer

API Communication: Custom hooks for task submission and status polling.

📂 Project Structure
Plaintext

src/
├── api/            # API service calls (summarizer.js)
├── components/     # Reusable UI components (TextInput, Loader, etc.)
├── pages/          # Main page views (Home.jsx)
├── App.jsx         # Root component
├── main.jsx        # Application entry point
└── index.css       # Global Tailwind directives
⚙️ Installation & Setup
Clone the repository:

Bash

git clone <your-repo-url>
cd hindi-text-summarizer
Install dependencies:

Bash

npm install
Run the development server:

Bash

npm run dev
The application will be available at http://localhost:5173.

📖 Usage
Paste your Hindi text (minimum 20 characters) into the input area.

Click the "सारांश बनाएँ" button.

The app will communicate with the backend API and poll for updates.

Once the process is complete, the summary will appear automatically in the output section.

⚠️ Error Handling
The application provides feedback in the following scenarios:

Input Validation: Alerts the user if the text is too short.

Server Issues: Notifies the user if the server connection fails or if an error occurs during processing.