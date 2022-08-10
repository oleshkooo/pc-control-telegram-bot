/**
 * @param {number} width
 * @description detect mobile device
 * @returns {boolean} true if mobile / false if not
 * @example
 * import useMobile from '...'
 * const isMobile = useMobile(768)
 */
const useMobile = (width) => {
    const { innerWidth } = window
    return innerWidth <= width
}
export default useMobile