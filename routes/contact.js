import express from 'express';
import { sendMail } from '../controllers/contact.js';


const router = express.Router();

router.post('/',sendMail);

export default router;
