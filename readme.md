**# iNote: Your Personal Note-Taking Oasis**

**Effortlessly capture and organize your thoughts with iNote, a powerful note-taking application built with FastAPI and MongoDB Atlas.**

## Features

- **Simple and intuitive interface**
- **Seamless note creation and editing**
- **Organize notes with tags and folders**
- **Full-text search to find notes quickly**
- **Dark mode for comfortable night-time note-taking**
- **Securely stored in MongoDB Atlas for reliability and scalability**

## Getting Started

1. **Prerequisites:**

   - Python 3.7 or later
   - MongoDB Atlas account
   - Git (optional, for cloning the repository)

2. **Installation:**

   ```bash
   git clone https://github.com/your-username/iNote.git
   cd iNote
   pip install -r requirements.txt
   ```

3. **Set up MongoDB Atlas:**

   - Create a MongoDB Atlas cluster.
   - Create a database and user for iNote.
   - Obtain the connection string for your database.

4. **Create a `.env` file:**

   ```
   MONGO_URI=your_mongodb_atlas_connection_string
   ```

5. **Run the application:**

   ```bash
   uvicorn index:app --reload
   ```

6. **Access iNote in your browser:**
   Typically at `http://127.0.0.1:8000/`

## Usage

- **Create a new note:** Click the "Submit" button to create a note with title and description.
- **Edit a note as Important:** Click on the Checkbox.
- **Search for notes:** comming soon.

## Connect with me on Linkedin

@ `https://www.linkedin.com/in/atharva-kawale-2002/`
