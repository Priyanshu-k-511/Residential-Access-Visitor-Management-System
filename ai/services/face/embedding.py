from pathlib import Path

import cv2
from insightface.app import FaceAnalysis


class FaceEmbedding:

    REQUIRED_MODEL_FILES = [
        "1k3d68.onnx",
        "2d106det.onnx",
        "det_10g.onnx",
        "genderage.onnx",
        "w600k_r50.onnx",
    ]

    def __init__(self):

        # ai/
        AI_DIR = Path(__file__).resolve().parents[2]

        # ai/models/buffalo_l/
        MODEL_DIR = AI_DIR / "models" / "buffalo_l"

        # to check if the model was installed
        missing_files = [
            file
            for file in self.REQUIRED_MODEL_FILES
            if not (MODEL_DIR / file).is_file()
        ]

        if missing_files:
            raise FileNotFoundError(
                "buffalo_l model is not installed correctly.\n"
                f"Missing files: {missing_files}\n"
                "Run setup_buffalo_l_model.py first."
            )

        # root=AI_DIR means InsightFace looks in:
        # ai/models/buffalo_l/
        self.app = FaceAnalysis(
            name="buffalo_l",
            root=str(AI_DIR),
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(ctx_id=-1)

    def get_embedding(self, image_path):

        image = cv2.imread(str(image_path))

        if image is None:
            raise ValueError(
                f"Unable to read image: {image_path}"
            )

        faces = self.app.get(image)

        if not faces:
            raise ValueError(
                "No face detected in the image."
            )

        # Select the largest face or closest face from the image
        face = max(
            faces,
            key=lambda f: (
                (f.bbox[2] - f.bbox[0])
                * (f.bbox[3] - f.bbox[1])
            )
        )

        embedding = face.embedding

        if embedding.shape[0] != 512:
            raise ValueError(
                f"Expected 512-D embedding, "
                f"got {embedding.shape[0]}-D."
            )

        return embedding