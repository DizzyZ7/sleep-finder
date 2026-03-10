async function search(){

let price=document.getElementById("price").value
let height=document.getElementById("height").value
let weight=document.getElementById("weight").value

let r=await fetch(`/api/filter?price=${price}&height=${height}&weight=${weight}`)

let data=await r.json()

let html=""

data.forEach(p=>{

html+=`
<div class="card">

<img src="${p.image}" width="200">

<h3>${p.name}</h3>

<p>${p.price}</p>

<a href="${p.link}" target="_blank">Открыть</a>

</div>
`
})

document.getElementById("results").innerHTML=html

}
