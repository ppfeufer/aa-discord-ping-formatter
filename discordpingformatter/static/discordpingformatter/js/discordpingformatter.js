jQuery(document).ready(function($) {
    var nl2br = (function(str, isXhtml) {
        var breakTag = (isXhtml || typeof isXhtml === 'undefined') ? '<br />' : '<br>';

        return (str + '').replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, '$1'+ breakTag +'$2');
    });

    /**
     * Closing the message
     *
     * @param {string} element
     * @returns {void}
     */
    var closeCopyMessageElement = (function(element) {
        /**
         * close after 5 seconds
         */
        $(element).fadeTo(5000, 500).slideUp(500, function() {
            $(this).slideUp(500, function() {
                $(this).remove();
            });
        });
    });

    /**
     * Show message when copy action was successfull
     *
     * @param {string} message
     * @param {string} element
     * @returns {undefined}
     */
    var showSuccess = (function(message, element) {
        $(element).html('<div class="alert alert-success alert-dismissable alert-copy-success"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' + message + '</div>');

        closeCopyMessageElement('.alert-copy-success');

        return;
    });

    /**
     * Show message when copy action was not successfull
     *
     * @param {string} message
     * @param {string} element
     * @returns {undefined}
     */
    var showError = (function(message, element) {
        $(element).html('<div class="alert alert-danger alert-dismissable alert-copy-error"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' + message + '</div>');

        closeCopyMessageElement('.alert-copy-error');

        return;
    });

    $('button#createPingText').on('click', function() {
        var pingType = $('select#pingType option:selected').val();
        var fleetType = $('select#fleetType option:selected').val();
        var fcName = $('input#fcName').val();
        var fleetName = $('input#fleetName').val();
        var formupLocation = $('input#formupLocation').val();
        var formupTime = $('input#formupTime').val();
        var fleetComms = $('input#fleetComms').val();
        var fleetDoctrine = $('input#fleetDoctrine').val();
        var fleetSrp = $('select#fleetSrp option:selected').val();
        var additinalInformation = $('textarea#additinalInformation').val();

        $('.aa-discord-ping-formatter-ping').show();

        var discordPingText = '';
        discordPingText += pingType + ' :: ';

        if(fleetType !== '') {
            discordPingText += '**' + fleetType + '** ';
        }

        discordPingText += 'Fleet is up' + "\n\n";

        if(fcName !== '') {
            discordPingText += '**FC:** ' + fcName + "\n";
        }

        if(fleetName !== '') {
            discordPingText += '**Fleet Name:** ' + fleetName + "\n";
        }

        if(formupLocation !== '') {
            discordPingText += '**Formup Location:** ' + formupLocation + "\n";
        }

        if(formupTime !== '') {
            discordPingText += '**Formup Time:** ' + formupTime + "\n";
        }

        if(fleetComms !== '') {
            discordPingText += '**Comms:** ' + fleetComms + "\n";
        }

        if(fleetDoctrine !== '') {
            discordPingText += '**Ships / Doctrine:** ' + fleetDoctrine + "\n";
        }

        if(fleetSrp !== '') {
            discordPingText += '**SRP:**' + fleetSrp + "\n\n";
        }

        if(additinalInformation !== '') {
            discordPingText += '**Additinal Information**: ' + "\n" + additinalInformation + "\n";
        }

        $('.aa-discord-ping-formatter-ping-text').html('<p>' + nl2br(discordPingText) + '</p>');
    });

    /**
     * Copy permalink to clipboard
     */
    $('button#copyDiscordPing').on('click', function() {
            /**
         * Copy permalink to clipboard
         *
         * @type Clipboard
         */
        var clipboardDiscordPingData = new Clipboard('button#copyDiscordPing');

        /**
         * Copy success
         *
         * @param {type} e
         */
        clipboardDiscordPingData.on('success', function(e) {
            showSuccess('Success, Ping copied to clipboard. Now be a good FC and throw it in your Discord so you actually get some people in fleet.', '.aa-discord-ping-formatter-ping-copyresult');

            e.clearSelection();
            clipboardDiscordPingData.destroy();
        });

        /**
         * Copy error
         */
        clipboardDiscordPingData.on('error', function() {
            showError('Error, Ping not copied to clipboard.', '.aa-discord-ping-formatter-ping-copyresult');

            clipboardDiscordPingData.destroy();
        });
    });
});
