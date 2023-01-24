var ctxMedia = document.getElementById('chartMedia')
var ctxAcertos = document.getElementById('chartAcertos')

//Gráfico de Média da turma//
var chartMedia = new Chart(ctxMedia, {
    type: 'bar',
    data: {
        labels: ['1° Período', '2°Período', '3° Período', '4° Período'],
        datasets: [{
            label: 'Média da Turma',
            data: [10, 60, 40, 80],
            backgroundColor: 'orange'
        }]
    },

    options: {
        responsive: true,  
        plugins: {
            legend: {
                labels: {
                    font: {
                        size: 19,
                        weight: 600
                    }
                }
            },

            title: {
                display: true,
                text: 'Análise por período',
                font: {
                    size: 38
                },
                color: 'black'
            }
        },

        scales: {
 
            x: {
                ticks: {
                    font: {
                        size: 15
                    }
                }
            },

            y: {
                ticks: {
                    font: {
                        size: 15
                    }
                }
            }

        }

    }

})

//Gráfico de Acertos por questão//
var chartAcertos = new Chart(ctxAcertos, {
    type: 'bar',
    data: {
        labels: ['1°', '2°', '3°', '4°', '5°', '6°', '7°', '8°', '9', '10°'],
        datasets: [{
            label: 'Alunos que acertaram',
            data: [10, 5, 22, 5, 30, 38, 43, 20, 12, 8],
            backgroundColor: 'orange'
        }]
    },

    options: {
        responsive: true,  
        plugins: {
            legend: {
                labels: {
                    font: {
                        size: 19,
                        weight: 600
                    }
                }
            },

            title: {
                display: true,
                text: 'Acertos por questão',
                font: {
                    size: 38
                },
                color: 'black'
            }
        },

        scales: {
 
            x: {
                ticks: {
                    font: {
                        size: 15
                    }
                }
            },

            y: {
                ticks: {
                    font: {
                        size: 15
                    }
                }
            }
        }    
    }    
})

//Botão voltar ao topo//
var btnTop = document.querySelector('.btn-top')

btnTop.addEventListener('click', function backToTop() {
    window.scrollTo(0, 0)
})

document.addEventListener('scroll', showBtnTop)

function showBtnTop() {
    if (window.scrollY > 50) {
        btnTop.style.display = 'block'
    } else {
        btnTop.style.display = 'none'
    }
}
