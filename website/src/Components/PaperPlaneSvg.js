import { motion } from 'framer-motion'

function PaperPlaneSvg() {
    const variants = {
        hidden: {
            opacity: 0,
            pathLength: 0,
            fill: "rgba(255, 255, 255, 0)",
        },
        visible: {
            opacity: 1,
            pathLength: 1,
            fill: "rgba(255, 255, 255, 1)",
            transition: {
                default: {
                    duration: 1,
                    ease: [1, 0, 0.8, 1],
                    delay: 2.5,
                },
                fill: {
                    duration: 1,
                    ease: [1, 0, 0.8, 1],
                    delay: 3,
                },
                opacity: {
                    duration: 1,
                    delay: 2,
                },
            }
        }               
    }

    return (
        <motion.svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            className="paper-plane-svg"
        >
            <motion.path
                d="M498.1 5.629C492.7 1.891 486.4 0 480 0a31.97 31.97 0 00-15.88 4.223l-448 255.1C5.531 266.3-.688 277.8.062 289.1s8.376 22.86 19.62 27.55l103.2 43.01 61.85 146.5C186.2 510.6 189.2 512 191.1 512a8.068 8.068 0 005.555-2.24l85.75-82.4 120.4 50.16a31.815 31.815 0 0012.29 2.472c6.615 0 12.11-2.093 15.68-4.097a31.995 31.995 0 0015.97-23.05l64-415.1C513.5 24.72 508.3 12.58 498.1 5.629zM32 288L412.1 70.8 123.9 326.3 32 288zm168.7 174.3l-49.6-117.4 229.5-203.4-169.5 233.1a16.016 16.016 0 00-2.438 13.84 15.925 15.925 0 009.438 10.41l34.4 13.76-51.8 49.69zm216-19L249 376.74l225.7-310.3-58 376.86z"
                variants={variants}
                initial="hidden"
                animate="visible"
            ></motion.path>
        </motion.svg>
    )
}

export default PaperPlaneSvg;
