const nodemailer = require('nodemailer');

const serverSupportMail = 'ddminh.19it5@vku.udn.vn'
const serverSupportPassword = 'apoqpzzgqnuhukct'

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: serverSupportMail,
    pass: serverSupportPassword
  }
});

function sendOptMail(email, otpCode){
  
  var mailOptions = {
    from: 'ddminh.19it5@vku.udn.vn',
    to: email,
    subject: 'Doi mat khau Ecommerce APP',
    text: 'Ma OTP doi mat khau: \n' + otpCode + '\nKhong chia se ma otp cho nguoi khac'
  };
  
  
  transporter.sendMail(mailOptions, function(error, info){
    if (error) {
      console.log(error);
    } else {
      console.log('Email sent: ' + info.response);
    }
  });    
  
}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; 
}


module.exports.sendOptMail = sendOptMail;
module.exports.getRandomInt = getRandomInt;



