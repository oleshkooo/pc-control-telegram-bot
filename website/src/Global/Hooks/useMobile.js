import { useEffect, useState } from 'react'

/**
 * @param {number} phoneWidth
 * @description detect mobile device
 * @returns {boolean} true if mobile / false if not
 * @example
 * import useMobile from '...'
 * const isMobile = useMobile(768)
 */
const useMobile = (phoneWidth) => {
    const [width, setWidth] = useState({})

    useEffect(() => {
        const updateWidth = () => setWidth(window.innerWidth)

        window.addEventListener('resize', updateWidth)
        updateWidth()

        return () => window.removeEventListener('resize', updateWidth)
    }, [])

    return width <= phoneWidth
}
export default useMobile