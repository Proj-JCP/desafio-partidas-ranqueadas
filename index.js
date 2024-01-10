function determinarNivel(jogador, vitorias, derrotas) {
    let resultado = vitorias - derrotas;
  
    if (resultado <= 10) {
      return "Ferro";
    } else if (resultado > 10 && resultado <= 20) {
      return "Bronze";
    } else if (resultado > 20 && resultado <= 50) {
      return "Prata";
    } else if (resultado > 50 && resultado <= 80) {
      return "Ouro";
    } else if (resultado > 80 && resultado <= 90) {
      return "Diamante";
    } else if (resultado > 90 && resultado <= 100) {
      return "Lendário";
    } else if (resultado > 100) {
      return "Imortal";
    }
  }
  
  let jogador = "julio ";
  let vitorias = 100;
  let derrotas = 5;
  let saldo = vitorias - derrotas

  let nivel = determinarNivel(jogador, vitorias, derrotas);
   
  console.log(jogador+ "tem o saldo de " + saldo + " pontos e está no nível " + nivel);