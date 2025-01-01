import mongoose from "mongoose";


 const userSchema = mongoose.Schema({
    userFullName: String,
    primaryImage: String,
    secondaryImage: String,
    userName: String,
    message: String,
    userEmail: String,
    userPhoneNumber: String,
    userGithub: String,
    userLinkedIn: String,
    userPassword: String,
    createdAt: {
        type: Date,
        default: new Date(),
    },
});

    const userMessage = mongoose.model('userMessage', userSchema);

export default userMessage;