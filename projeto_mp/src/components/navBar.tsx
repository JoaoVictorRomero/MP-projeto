import Styles  from "@/styles/navBar.module.css"
export default function NavBar(){
    return(
    <header className={Styles.header}>
          <div>
            <a href=""><img src="/WhatsApp_Image_2023-11-24_at_15.20 1.png" alt="" /></a>
          </div>

          <div className={Styles.div_links}>
            <a className={Styles.a} href="/Buscar">Buscar</a>
            <a  className={Styles.PratosDia} href="/PratosDoDia">Pratos do Dia</a>
            <a className={Styles.a} href="/Mapa">Mapa</a>
          </div>

          <div>
            <a className={Styles.a} href="/Login">Login</a>
          </div>
    </header>
    )
}