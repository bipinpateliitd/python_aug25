# ✅ Git for Windows: Installation and Setup Guide (with SSH and Global Config)

This guide helps you install **Git on Windows** and configure it with **SSH authentication** for GitHub, including all essential global settings.

---

## 🔹 Step 1: Download Git

1. Visit: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Download will start automatically (e.g., `Git-2.44.0-64-bit.exe`)

---

## 🔹 Step 2: Install Git with Recommended Settings

During installation, use these settings:

| Screen | Recommended Option |
|--------|---------------------|
| **Select Components** | ✅ All default |
| **Editor** | ✅ Visual Studio Code (or Notepad++) |
| **PATH setting** | ✅ Git from command line and 3rd-party software |
| **HTTPS transport** | ✅ Use HTTPS |
| **Line endings** | ✅ Checkout Windows-style, commit Unix-style |
| **Terminal emulator** | ✅ Use MinTTY (default) |
| **Extra options** | ✅ Enable file system caching |
| **Experimental features** | ❌ Leave unchecked |

---

## 🔹 Step 3: Configure Git (One-Time)

Open **Git Bash** and run:

```bash
git config --global user.name "sanket"
git config --global user.email "sanket@gmail.com"
git config --global core.editor "code --wait"
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global color.ui auto
git config --global credential.helper manager-core

git config --global --list

## 🔹 Step 4: Set Up SSH for GitHub
ssh-keygen -t ed25519 -C "sanket@gmail.com"

#Press Enter to accept default path

#Press Enter twice to skip passphrase

# Start SSH Agent and Add Key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

## 🔹 Step 5: Add SSH Key to GitHub

cat ~/.ssh/id_ed25519.pub

Copy the output.

#Go to https://github.com/settings/ssh/new

#Paste the key and give it a title (e.g., My Laptop SSH)

#Save.
#Step 6: Test SSH ConnectionStep 6: Test SSH Connection
ssh -T git@github.com




