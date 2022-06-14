const jwt = require('jsonwebtoken')

module.exports = (req, res, next)=>{
    try{
        const token = req.headers.authorization
        console.log(token)
        const decoded = jwt.verify(token, process.env.JWT_SECRET_KEY);
        req.userData = decoded;
        console(decoded)
        next()
    }
    catch(error){
        return res.status(401).json({
            message:'Token khong hop le'
        })
    }
}