import mongoose from "mongoose";

 const skillSchema = mongoose.Schema({
    skillName: String,
    skillExperience: String,
    createdAt: {
        type: Date,
        default: new Date(),
    },
});
    const skillMessage = mongoose.model('skillMessage', skillSchema);

export default skillMessage;