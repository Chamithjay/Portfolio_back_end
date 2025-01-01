import express from 'express';
import { getProjects,addProjects } from '../controllers/projects.js';

const router = express.Router();

router.get('/', getProjects);
router.post('/', addProjects);

export default router;