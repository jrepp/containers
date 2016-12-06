announce
    service-desc
        name
        site
        created
        modified
        scope [global,region,game]
        ip
        ports
        service-class
        provides
        role [leader,member,promoting,demoting]
        commands/
        vars-source/
        vars/

serice-structure
    /services
        global/
        region-name/
            site-name/

variable-templates
    /name
        vars

cluster-desc
    name
    state [starting, active, host-error, stopping, stopped]
    leader
    created
    modified
    min-count
    max-count
    members []
    joining []
    leaving []
    commands/
    partition/
        type
        key

command-desc
    name
    args []
    user
    created
    acknowledged
    pending
    duration
    complated

command-structure
    commands/
        pending/
        running/
        completed/

lifecycle
    starting
    started
    activating
    active
    draining/filling
    drained/filled
    stopping
    stopped

discovery
    by-type
    by-name
    by-provides
    by-site
    only-local

join-domain
    add-to-joiners
    accept-from-joiners        

leave-domain
    add-to-leavers
    accept-from-leavers

    
