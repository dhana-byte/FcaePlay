# 🎮 FacePlay - Emotion-Based Jet Shooting Game

**FacePlay** is an innovative jet shooting game built with Python and Pygame that adapts its difficulty in real-time based on the player’s mood using AI-powered emotion detection from the webcam 🎯.

---

## 📸 How It Works

Using **DeepFace** (a powerful facial analysis framework), the game reads your emotion through your webcam every 10 seconds and adjusts difficulty levels accordingly:

| Emotion       | Game Difficulty |
|---------------|------------------|
| 😊 Happy       | Hard (more enemies) |
| 😡 Angry / 😢 Sad / 😱 Fear | Easy |
| 😐 Neutral / Unknown | Medium |

---

## 🧠 Tech Stack

- 🐍 **Python 3**
- 🕹 **Pygame** for game development
- 📷 **OpenCV** for webcam feed
- 🤖 **DeepFace** for real-time emotion recognition
- 🎨 Custom 2D game design with jet sprites

---
                ┌─────────────────────┐
                │   User Webcam Feed  │
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │  DeepFace + OpenCV  │  ← Detect Emotion
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │  Global Game State  │  ← Update difficulty level
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │     Game Engine     │  ← Pygame logic, drawing, movement
                └─────────┬───────────┘
                          ↓
                ┌─────────────────────┐
                │      Main Loop      │  ← Updates display and handles exit
                └─────────────────────┘


## 🗂 Project Structure

faceplay/ ├── assets/ │ └── jet.png # Jet image ├── src/ │ ├── main.py # Game loop and Pygame window │ ├── emotion_detector.py # DeepFace-based emotion detection │ ├── game_engine.py # Game mechanics and logic │ └── globals.py # Shared game variables ├── requirements.txt # Python dependencies ├── README.md # You're here!
