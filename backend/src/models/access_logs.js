const mongoose = require("mongoose");

const accessLogSchema = new mongoose.Schema(
  {
    eventType: {
      type: String,
      enum: ["entry", "exit"],
      required: true
    },
    personType: {
      type: String,
      enum: ["resident", "visitor", "unknown"],
      required: true
    },
    residentId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "residents",
      default: null
    },
    visitorId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "visitors",
      default: null
    },
    visitingFlat: {
      type: String,
      default: null,
      trim: true
    },
    vehicleNumber: {
      type: String,
      default: null,
      trim: true
    },
    recognition: {
      face: {
        detected: {
          type: Boolean,
          required: true
        },
        matched: {
          type: Boolean,
          required: true
        },
        confidence: {
          type: Number,
          default: null,
          min: 0,
          max: 1
        }
      },
      licensePlate: {
        detected: {
          type: Boolean,
          required: true
        },
        matched: {
          type: Boolean,
          required: true
        },
        confidence: {
          type: Number,
          default: null,
          min: 0,
          max: 1
        }
      }
    },
    accessDecision: {
      type: String,
      enum: ["allowed", "denied", "pending"],
      required: true
    },
    gateId: {
      type: String,
      required: true,
      trim: true
    },
    timestamp: {
      type: Date,
      default: Date.now,
      required: true
    }
  }
);

module.exports = mongoose.model("AccessLog", accessLogSchema);