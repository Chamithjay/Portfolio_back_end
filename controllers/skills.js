import SkillMessage from '../models/skillMessage.js';

export const getSkills = async (req, res) => {
    try {
        const skills = await SkillMessage.find(); 
        res.status(200).json(skills); 
    } catch (error) {
        res.status(500).json({ message: error.message }); 
    }
}

export const addSkills = async(req,res)=>{
    const skill = req.body;
    const newSkill = new SkillMessage(skill);
    try {
        await newSkill.save();
        res.status(201).json(newSkill);
    } catch (error) {
        res.status(409).json({ message: error.message });
    }
}