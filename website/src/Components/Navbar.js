import { useEffect } from 'react'
import { Link } from 'react-scroll'
import { motion } from 'framer-motion'
import useMobile from '../Global/Hooks/useMobile'
import useDisableBodyScroll from '../Global/Hooks/useDisableBodyScroll'

import PaperPlaneSvg from './PaperPlaneSvg'
import { useState } from 'react'

const duration = 10
const links = [
    { to: 'home', text: 'Home' },
    { to: 'about', text: 'About' },
    { to: 'projects', text: 'Projects' },
    { to: 'contact', text: 'Contact' },
]

const Navbar = () => {
    const isMobile = useMobile(768)

    const [isOpen, setOpen] = useState(false)
    const openMenu = () => setOpen(true)
    const closeMenu = () => setOpen(false)
    
    // ? close menu on scroll
    useEffect(() => {
        window.addEventListener('scroll', closeMenu)
        return () => window.removeEventListener('scroll', closeMenu)
    }, [])
    // ? disable body scroll while menu is open
    // useDisableBodyScroll(isOpen)
    // ? close menu on 'escape'
    useEffect(() => {
        const escClose = (e) => {
            if (e.keyCode === 27) // escape
                closeMenu()
        }
        window.addEventListener('keydown', escClose)

        return () => window.removeEventListener('keydown', escClose)
    }, [])
    
    const linksArr = isMobile ?
    links.map(({ to, text }) => (
        <Link key={to} to={to} smooth={true} duration={duration} onClick={closeMenu} className="my-3 text-shadow">
            <motion.p 
                whileTap={{
                    scale: 0.92,
                }}
            >{text}</motion.p>
        </Link>
    ))
    :
    links.map(({ to, text }) => (
        <Link key={to} to={to} smooth={true} duration={duration} className="mx-3 text-shadow">
            <motion.p
                whileTap={{
                    scale: 0.92,
                }}
            >{text}</motion.p>
        </Link>
    ))

    const variants = {
        open: {
            x: '20%',
        },
        closed: {
            x: '110%',
        },
        transition: {
            type: 'spring',
            stiffness: 200,
            damping: 20,
        },
    }

    return (
        <>
            {isMobile && 
                <motion.div
                    id="menu"
                    variants={variants}
                    initial="closed"
                    animate={isOpen ? 'open' : 'closed'}
                    transition={variants.transition}
                    onClick={closeMenu}
                >
                    <div
                        className="menu-inner"
                        onClick={(e) => e.stopPropagation()}
                    >
                        <div className="links">
                            <div className="visible">
                                {linksArr}
                            </div>
                        </div>
                    </div>
                </motion.div>
            }

            <motion.div
                id="navbar"
                className="pt-4"
                initial={{
                    y: '-50vh',
                }}
                animate={{
                    y: 0,
                }}
                transition={{
                    type: 'spring',
                    duration: 1,
                    delay: 0.5,
                }}
            >
                <div className="container pt-2">
                    <div className="nav">
                        <div className="logo">
                            <Link to="home" smooth={true} duration={duration}>
                                <PaperPlaneSvg />
                                <h1 className="navbar-brand text-shadow fw-bold mx-3">{process.env.REACT_APP_NAME}</h1>
                            </Link>
                        </div>
                        <div className="links pt-1">
                            {isMobile ?
                            <>
                                <motion.button
                                    className="btn-bars"
                                    onClick={openMenu}
                                    whileHover={{
                                        scale: 1.08,
                                    }}
                                    whileTap={{
                                        scale: 0.9,
                                    }}
                                >
                                    <h2>
                                        <i className="fa-solid fa-bars" />
                                    </h2>
                                </motion.button>
                            </>
                            : linksArr}
                        </div>
                    </div>
                </div>
            </motion.div>
        </>
    )
}
export default Navbar