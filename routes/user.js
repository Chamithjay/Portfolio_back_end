import express from 'express';
import { getUser, updateUser,loginUser } from '../controllers/user.js';

const router = express.Router();

router.get('/', getUser);
router.post('/', updateUser);
router.post('/login', loginUser);

export default router;