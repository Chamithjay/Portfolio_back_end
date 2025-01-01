import ProjectMessage from '../models/projectMessage.js';


export const getProjects = async (req, res) => {
    try {
        const projects = await ProjectMessage.find(); 
        res.status(200).json(projects); 
    } catch (error) {
        res.status(500).json({ message: error.message }); 
    }
}

export const addProjects = async (req, res) => {
    const project = req.body;
    const newProject = new ProjectMessage(project);
    try {
        await newProject.save();
        res.status(201).json(newProject);
    } catch (error) {
        res.status(409).json({ message: error.message });
    }
}