-- CreateExtension
CREATE EXTENSION IF NOT EXISTS "vector";

-- CreateTable
CREATE TABLE "Resident" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "flatNo" TEXT NOT NULL,
    "faceEmbedding" vector(512) NOT NULL,
    "status" BOOLEAN NOT NULL DEFAULT true,

    CONSTRAINT "Resident_pkey" PRIMARY KEY ("id")
);
