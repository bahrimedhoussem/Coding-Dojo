const AuthorController = require ("../controllers/author.controller")
module.exports = (app) => {
    app.get('/api/authors' , AuthorController.getAll)
    app.post('/api/authors/new' , AuthorController.create)
    app.put('/api/authors/:id/update' , AuthorController.update)
    app.delete('/api/authors/:id' , AuthorController.delete)
}