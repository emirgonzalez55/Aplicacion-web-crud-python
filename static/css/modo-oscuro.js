const tematable = document.getElementById('tematable');
const modooscuro = document.getElementById('modooscuro');
const boton = document.querySelector('#boton');
const localConfig = localStorage.getItem('tema');


if (localConfig === 'dark') {
    modooscuro.classList.add('modo-oscuro')
    tematable.classList.add('table-dark')

} else if (localConfig === 'light') {
    modooscuro.classList.remove('modo-oscuro')
    tematable.classList.remove('table-dark')
}
boton.addEventListener('click', () => {
    let colorTema;
    if (modooscuro.classList.contains('modo-oscuro')){
        modooscuro.classList.remove('modo-oscuro')
        tematable.classList.remove('table-dark')
        colorTema = 'light'

    }else {
        modooscuro.classList.add('modo-oscuro',)
        tematable.classList.add('table-dark')
        colorTema = 'dark'
    }
    localStorage.setItem('tema', colorTema)
}) 
    
