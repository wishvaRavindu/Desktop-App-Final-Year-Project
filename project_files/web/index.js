
document.getElementById("InitiateDetection").addEventListener("click",async() =>{
    await eel.video_feed();
})

document.getElementById("close_detection").addEventListener("click",async() =>{
    await eel.closeDetection();
})

//document.getElementById("viewDetection").addEventListener("click",async() =>{
//    await eel.showDetection();
//})
//
//document.getElementById("openCamera").addEventListener("click",async() =>{
//    await eel.openCameraModule();
//})

//
//function py_video() {
//    eel.video_feed()()
//}
//
//
eel.expose(updateImageSrc);
function updateImageSrc(val) {
    let elem = document.getElementById('bg');
    elem.src = "data:image/jpeg;base64," + val
}
