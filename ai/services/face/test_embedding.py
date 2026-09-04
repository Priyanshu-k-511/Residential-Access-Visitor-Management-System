from pathlib import Path

from embedding import FaceEmbedding

PROJECT_DIR = Path(__file__).resolve().parents[3]

image_path = PROJECT_DIR / "database" / "faces" / "Priyanshu_pic.jpeg"

face_embedding = FaceEmbedding()

embedding = face_embedding.get_embedding(image_path)

print("Embedding generated successfully")
print("Shape:", embedding.shape)
print(embedding)