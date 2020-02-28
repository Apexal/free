

const app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        crns: [],
        newCRN: '',
        changed: false,
        calendar: null,
        timeoutID: null
    },
    mounted() {
        if (localStorage.getItem('crns') !== null) {
            try {
                this.crns = JSON.parse(localStorage.getItem('crns'))
            } catch (e) {
                localStorage.removeItem('crns')
            }
        }

        // Setup calendar
        this.calendar = new FullCalendar.Calendar(this.$refs.calendar, {
            plugins: ['dayGrid', 'timeGrid'],
            defaultView: 'timeGridWeek',
            events: async () => {
                if (this.crns.length === 0) return []

                const response = await fetch('/events?crns=' + this.crns.join(','))
                const events = await response.json()
                this.changed = false
                return events
            },
            header: {
                left: '',
                center: '',
                right: ''
            },
            columnHeaderFormat: {
                weekday: 'long'
            },
            slotDuration: '01:00:00',
            allDaySlot: false,
            minTime: '08:00:00',
            maxTime: '20:00:00',
            height: '100%'
        })

        this.calendar.render()
    },
    watch: {
        crns (newCRNS) {
            this.changed = true
            localStorage.setItem('crns', JSON.stringify(newCRNS))

            clearTimeout(this.timeoutID)
            this.timeoutID = setTimeout(() => {
                this.calendar.refetchEvents()
            }, 1500)
        }
    },
    methods: {
        update () {
            this.changed = true
            this.calendar.refetchEvents()
        },
        addCRNS () {
            const newCRNS = this.newCRN.trim()
                .replace(/,/g, ' ')
                .replace(/\n/g, ' ')
                .split(' ')
                .filter(val => !!val)
                .map(val => val.trim())
                .filter(val => !isNaN(parseFloat(val)) && isFinite(val))

            this.crns.push(...newCRNS)
            
            this.newCRN = ''
        }
    }
})
