var ctxMedia = document.getElementById('chartMedia')
var ctxAcertos = document.getElementById('chartAcertos')

labels = labels.slice(1, -1).replaceAll("&#x27;", "")
labels = labels.split(",")


//Gráfico de Média da turma//
var chartMedia = new Chart(ctxMedia, {
    type: 'bar',
    data: {
        labels: ['1° Período', '2°Período', '3° Período', '4° Período'],
        datasets: [{
            label: 'Média da Turma',
            data: dados,
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
                text: 'Análise por período - ' + turma,
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
        labels: labels,
        datasets: [{
            label: 'Alunos que acertaram',
            data: [10, 5, 22, 5, 30, 38, 43, 20, 12, 8],
            backgroundColor: 'greenyellow'
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

var destination;

var tr = function() {
    var url = window.location.href.toString();
    window.location.href = url.replace("dashboard", destination);
}

function Red(d) {
    destination = d;
    if (destination == "turmas") {
        document.cookie = "voltou=0" + ";path=/";
    }
    document.getElementById("load-div-container").style.display = "flex";
    setTimeout(tr, 1000);
}