const {Author} = require ("../models/author.model")


module.exports.getAll = (req , res) => {
    Author.find({})
    .then(objs => res.json (objs))
    .catch(err => res.json(err))
}

module.exports.create = (req , res) => {
    Author.create(req.body)
    .then(obj => res.json(obj))
    .catch(err => res.status(400).json(err) )
}

module.exports.update = (req,res) => {
    Author.findOneAndUpdate({_id:req.params.id}, req.body , {new:true , runValidators : true})
    .then(obj=>res.json(obj))
    .catch(err => res.status(400).json(err))
}

module.exports.delete = (req,res) => {
    Author.deleteOne({_id:req.params.id})
    .then(obj=>res.json(obj))
    .catch(err=>res.json(err))
}