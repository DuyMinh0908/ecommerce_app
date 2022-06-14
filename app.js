const express = require('express')
const bodyParser = require('body-parser')
require('dotenv').config();

const app = express()
app.use('/storage_product', express.static('storage_product'));
app.use('/storage_user', express.static('storage_user'));
app.use('/storage_poster', express.static('storage_poster'));

const userRouter = require('./api/routes/users')
const productRouter = require('./api/routes/products')
const favoriteRouter = require('./api/routes/favorites')
const cartRouter = require('./api/routes/carts')
const historyRouter = require('./api/routes/history')
const reviewRouter = require('./api/routes/review')
const posterRouter = require('./api/routes/posters')
const addressRouter = require('./api/routes/address')
const orderRouter = require('./api/routes/orders')
const port = 3000
app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())
app.use('/users', userRouter)
app.use('/products',productRouter)
app.use('/favorites',favoriteRouter)
app.use('/carts',cartRouter)
app.use('/history',historyRouter)
app.use('/review',reviewRouter)
app.use('/posters',posterRouter)
app.use('/address',addressRouter)
app.use('/orders',orderRouter)
app.listen(port, () => console.log("Server Started"))