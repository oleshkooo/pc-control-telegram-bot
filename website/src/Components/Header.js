import { motion } from 'framer-motion'

import Navbar from './Navbar'
import IconSvg from './IconSvg'

const duration = 10

const Header = () => {

    return (
        <>
            <div id="header">

                <Navbar />

                <div className="container">
                    <div className="inner">
                        <motion.div
                            className="left top"
                            initial={{
                                y: '-100vh',
                            }}
                            animate={{
                                y: 0,
                            }}
                            transition={{
                                type: 'spring',
                                duration: 1,
                                delay: 1,
                            }}
                        >
                            <h1 className="display-2 fw-bold">Control your PC</h1>
                            <h1 className="display-6 fw-normal pt-2">using our application</h1>
                        </motion.div>
                        <motion.div
                            className="right bottom"
                            initial={{
                                y: '-150vh',
                            }}
                            animate={{
                                y: 0,
                            }}
                            transition={{
                                type: 'spring',
                                duration: 1,
                                delay: 1.5,
                            }}
                        >
                            <IconSvg />
                        </motion.div>
                    </div>
                </div>
            </div>
        </>
    )
}
export default Header