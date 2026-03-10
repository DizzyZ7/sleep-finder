async function search(){

let w=document.getElementById("weight").value
let h=document.getElementById("height").value
let p=document.getElementById("price").value

let res=await fetch(`/api/filter?weight=${w}&height=${h}&price=${p}`)

let data=await res.json()

let html=""

data.forEach(item=>{
html+=`
<div class="card">
<h3>${item.name}</h3>
<p>Цена: ${item.price}</p>
<p>Высота: ${item.height} см</p>
</div>
`
})

document.getElementById("results").innerHTML=html

}
