import UserMessage from '../models/userMessage.js';
import jwt from 'jsonwebtoken';
import dotenv from 'dotenv';

dotenv.config()


export const getUser = async (req, res) => {
    try {
        const user = await UserMessage.findOne(); 
        res.status(200).json(user); 
    } catch (error) {
        res.status(500).json({ message: error.message }); 
    }
}

export const updateUser = async (req, res) => {
    const user = req.body;

    try {
        // Update the user or create a new one if it doesn't exist
        const updatedUser = await UserMessage.findOneAndUpdate(
            {}, // Find any user (assuming single admin user scenario)
            user,
            { new: true, upsert: true } // Return updated document and create if not found
        );

        // Ensure only one user remains in the database
        await UserMessage.deleteMany({ _id: { $ne: updatedUser._id } });

        res.status(201).json(updatedUser);
    } catch (error) {
        res.status(409).json({ message: error.message });
    }
};

export const loginUser = async (req, res) => {
    const { userName, userPassword } = req.body;

    try {
        // Validate inputs
        if (!userName || !userPassword) {
            return res.status(400).json({ message: "Username and password are required" });
        }

        // Find user by username
        const user = await UserMessage.findOne({ userName });
        if (!user) {
            return res.status(404).json({ message: "User not found" });
        }

        // Compare plain-text passwords
        if (userPassword !== user.userPassword) {
            return res.status(401).json({ message: "Invalid password" });
        }

        // Generate JWT token
        const token = jwt.sign(
            { id: user._id, userName: user.userName },
            process.env.SECRET_KEY,
            { expiresIn: "30m" }
        );

        res.status(200).json({
            success: true,
            message: "Login successful",
            token,
        });
    } catch (error) {
        console.error("Error during login:", error); // Log error for debugging
        res.status(500).json({ message: "Internal server error" });
    }
};
