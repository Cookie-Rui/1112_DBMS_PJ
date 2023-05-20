// 獲取HTML物件
// 以及初始化
const MinorButton = document.getElementById("Minor");
const MinorBlock = document.getElementById("MinorBlock")
MinorBlock.style.display = "none"
// 功能

// 當點擊是否有雙主修按鈕後
// 可以拓展出額外的輸入空間
MinorButton.addEventListener('change', (event)=>{
    if(event.target.checked){
        MinorBlock.style.display = "block"
    }else{
        MinorBlock.style.display = "none"
    }
})