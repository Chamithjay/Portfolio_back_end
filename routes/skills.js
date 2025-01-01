import express from 'express';
import { addSkills, getSkills } from '../controllers/skills.js';

const router = express.Router();

router.post('/', addSkills);
router.get('/', getSkills);

export default router;