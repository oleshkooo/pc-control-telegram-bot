import { useEffect } from 'react'

/**
 * @param {boolean} isOpen disable body scroll, e.g. when modal window is open
 * @example
 * import useDisableBodyScroll from '...'
 * let isOpen = false
 * useDisableBodyScroll(isOpen)
 */
const useDisableBodyScroll = (isOpen) => {
    useEffect(() => {
        const body = document.body

        if (isOpen) {
            body.style.overflow = 'hidden'
        }
        else {
            body.style.overflow = 'unset'
        }
    }, [isOpen])
}
export default useDisableBodyScroll