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

## 🗂 Project Structure

