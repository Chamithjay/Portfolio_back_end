
import nodemailer from 'nodemailer';


export const sendMail = async (req, res) => {
    const transporter = nodemailer.createTransport({
        service:'gmail',
        auth:{
            user:process.env.GMAIL,
            pass:process.env.GMAIL_PASSWORD,
        }
    })
    const mailoptions = {
        from: req.body.email,
        to: process.env.GMAIL,
        subject:`${req.body.name}:${req.body.subject}`,
        text: req.body.message

    }
    transporter.sendMail(mailoptions, (error, info)=>{
        if(error){
            console.log("error",error);
            res.send('error');
        }
        else{
            console.log("success");
            res.send("success");
        }
    })
        
}