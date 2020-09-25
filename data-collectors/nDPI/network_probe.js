const {exec}  = require('child_process')
const redis = require('redis')
const fs = require('fs')
const yargs = require('yargs');

const client = redis.createClient();
const argv = yargs
    .option('interface', {
        alias: 'i',
        description: 'select interface',
        type: 'string',
        required: true
    })
    .help()
    .alias('help', 'h')
    .argv;
const writeThroughCache = () =>{
    return new Promise((resolve,reject)=>{
        exec(`sudo ndpiReader -C debug.csv -P 4:8:10:128:25 -i ${argv.interface} -s 10`,(err,stdout,stderr)=>{
            console.log("start")
            let i = 0;
            fs.createReadStream("debug.csv")
            .on('data',(d)=>{
                console.log(d)
                client.xadd("DATASTREAM","*","csv",d);
            })
            .on('end',()=>{
                resolve("done")
            })
            .on('error',(error)=>reject(err))

                
    })
})
}

const service = ()=>{
    setInterval( ()=>{
        writeThroughCache().then(console.log).catch(console.log)
    },10000)
}


if(argv.interface) service()
else console.log('Please Select Network Interface')