import mongoose from "mongoose";


 const projectSchema = mongoose.Schema({
    projectName: String,
    projectImage: String,
    projectLink: String,
    createdAt: {
        type: Date,
        default: new Date(),
    },
    likeCount: {
        type: Number,
        default: 0,
    },
});
    const ProjectMessage = mongoose.model('ProjectMessage', projectSchema);

export default ProjectMessage;