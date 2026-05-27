# Upload This SQL Practice Pack to GitHub

## 1. Create or Sign In to GitHub

Create an account or sign in at:

https://github.com

## 2. Install Git on macOS

Run:

```bash
xcode-select --install
```

After installation, confirm Git works:

```bash
git --version
```

## 3. Configure Git

Use your GitHub username and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## 4. Create a GitHub Repository

On GitHub, create a new repository, for example:

```text
sql-practice-questions
```

Do not initialize it with a README if you want to push this folder as-is.

## 5. Commit and Push

From this project folder:

```bash
cd /Users/nishukolimi/Documents/Codex/2026-05-27/for-data-engineer-interview-prep-need
git init
git add sql-practice-questions
git commit -m "Add SQL practice questions for data engineering interviews"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sql-practice-questions.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

