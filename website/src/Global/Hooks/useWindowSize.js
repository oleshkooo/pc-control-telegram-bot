/**
 * @param {void}
 * @return {object} { width, height }
 * @description returns the width and height of the window
 * @example
 * import useWindowSize from '...'
 * const { width, height } = useWindowSize()
 * // or
 * const width = useWindowSize().width
 * const height = useWindowSize().height
 */
const useWindowSize = () => {
    const { innerWidth: width, innerHeight: height } = window
    return {
        width,
        height
    }
}
export default useWindowSize